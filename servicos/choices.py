from django.db.models import TextChoices

class ChoicesCategoriaManuntencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "trocar válcula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"