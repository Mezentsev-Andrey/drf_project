import django_filters.rest_framework
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_product, create_stripe_session, convert_rub_to_usd


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(owner=self.request.user)
        product_name = payment.paid_course.name
        stripe_product = create_stripe_product(product_name)
        amount_in_usd = convert_rub_to_usd(payment.paid_course.price)
        stripe_price = create_stripe_price(stripe_product, amount_in_usd)
        session_id, payment_link = create_stripe_session(stripe_price)
        payment.payment_amount = amount_in_usd
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PaymentlListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = ["course", "lesson", "payment_type"]
    ordering_fields = ["date"]
