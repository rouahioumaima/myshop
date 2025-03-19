from django import forms  # Importation du module des formulaires Django
from .models import Commande  # Importation du modèle Commande défini dans models.py
# Définition du formulaire basé sur le modèle Commande
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande  # Spécification du modèle sur lequel se base le formulaire
        fields = [  # Liste des champs du modèle à inclure dans le formulaire
            'quantity', 'payment', 'customer_name', 
            'customer_email', 'customer_phone', 'customer_address',
        ]
        # Définition des labels (noms affichés) pour chaque champ dans le formulaire
        labels = {
            'quantity': 'Quantité',  # Nom du champ quantity affiché en français
            'payment': 'Mode de paiement',  # Nom du champ payment
            'customer_name': 'Nom complet',  # Nom du champ customer_name
            'customer_email': 'Email',  # Nom du champ customer_email
            'customer_phone': 'Téléphone',  # Nom du champ customer_phone
            'customer_address': 'Adresse',  # Nom du champ customer_address
        }

        # Définition des widgets pour personnaliser l'apparence des champs dans le formulaire HTML
        widgets = {
            'quantity': forms.NumberInput(attrs={  # Champ de type nombre avec classe Bootstrap et placeholder
                'class': 'form-control', 
                'placeholder': 'Quantité'
            }),
            'payment': forms.Select(attrs={  # Champ de sélection avec classe Bootstrap
                'class': 'form-control'
            }),
            'customer_name': forms.TextInput(attrs={  # Champ de texte avec classe Bootstrap et placeholder
                'class': 'form-control', 
                'placeholder': 'Nom complet'
            }),
            'customer_email': forms.EmailInput(attrs={  # Champ email avec classe Bootstrap et placeholder
                'class': 'form-control', 
                'placeholder': 'Email'
            }),
            'customer_phone': forms.TextInput(attrs={  # Champ texte avec classe Bootstrap et placeholder
                'class': 'form-control', 
                'placeholder': 'Téléphone'
            }),
            'customer_address': forms.Textarea(attrs={  # Champ textarea pour l'adresse avec classe Bootstrap et placeholder
                'class': 'form-control', 
                'placeholder': 'Adresse'
            }),
        }



