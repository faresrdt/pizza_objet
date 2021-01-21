class Pizza:
    def __init__(self, nom, prix, ingredients, veggie=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.veggie = veggie

    def Afficher(self):
        veg_str = ""
        if self.veggie:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()


class PizzaPersonnalisee(Pizza):

    prix_de_base = 7
    prix_un_ingredient = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.num_pizza = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée n°" + str(self.num_pizza), 0, [])
        self.demander_ingredient_utilisateur()
        self.calculer_le_prix(self.ingredients)
        self.numero_pizza = 0

    def demander_ingredient_utilisateur(self):
        print("-------------------")
        print(f"Ingrédients pour la pizza personnalisée n°{self.num_pizza}")
        while True:
            ingredient = input("Ajouter un ingredient (ou appuyez sur ENTRER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self, ingredients):
        self.prix = self.prix_de_base + (self.prix_un_ingredient * len(ingredients))
        return self.prix


pizzas = [
    Pizza("4 fromage", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Basilica Poulet", 9.5, ("mozzarella", "poulet rôti", "oignons", "tomate", "tomates cerises")),
    Pizza("Urban Kebab", 11.5, ("mozzarella", "viande kebab", "merguez", "oignons", "sauce blanche")),
    Pizza("Basilica Veggie", 10.5, ("mozzarella", "émincé végétal rôti", "oignons", "tomate"), True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee(),
    PizzaPersonnalisee(),

]


def tri(e):
    return e.nom


# pizzas.sort(key=tri)

# AFFICHIER UNIQUEMENT LES PIZZAS VEGGIES
# for i in pizzas:
#     if i.veggie:
#         i.Afficher()
# AFFICHIER UNIQUEMENT LES PIZZAS NON VEGGIES
# for i in pizzas:
#     if not i.veggie:
#         i.Afficher()
# AFFICHIER UNIQUEMENT LES PIZZAS QUI ONT DE LA TOMATE
# for i in pizzas:
#     if "tomate" in i.ingredients:
#         i.Afficher()
# AFFICHIER UNIQUEMENT LES PIZZAS QUI SONT EN DESSOUS DE 10€
# for i in pizzas:
#     if i.prix < 10:
#         i.Afficher()
for i in pizzas:
    i.Afficher()
