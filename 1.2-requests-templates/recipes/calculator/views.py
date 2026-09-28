from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_servings(request):
    try:
        servings = int(request.GET.get('servings', 1))
    except ValueError:
        return 1
    return servings if servings > 0 else 1


def recipe_view(request, dish):
    servings = get_servings(request)
    recipe = {
        ingredient: round(amount * servings, 2)
        for ingredient, amount in DATA.get(dish, {}).items()
    }
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)
