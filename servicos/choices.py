from django.db.models import TextChoices

class ChoicesCategoriaManuntencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "trocar válcula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"
    GEOMETRIA = "GEO", "Geometria"
    TROCA_DISCO_FREIO = "TDF", "Troca de disco de freio"
    TROCA_VELA = "TV", "Troca de vela"
    TROCA_FAROLETE ="TF", "Troca do farol frontal"
    TROCA_SINALEIRA = "TS", "Troca do farol traseiro"