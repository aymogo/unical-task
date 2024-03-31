from django.contrib import admin


class PriceRangeFilter(admin.SimpleListFilter):
    """Filer by price range"""

    title = "Ценовой диапазон"
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        return (
            ("0-100", "0 - 100"),
            ("100-500", "100 - 500"),
            ("500-1000", "500 - 1000"),
            ("1000-", "1000+"),
        )

    def queryset(self, request, queryset):
        if self.value() == "0-100":
            return queryset.filter(price__range=(0, 100))
        elif self.value() == "100-500":
            return queryset.filter(price__range=(100, 500))
        elif self.value() == "500-1000":
            return queryset.filter(price__range=(500, 1000))
        elif self.value() == "1000-":
            return queryset.filter(price__gte=1000)
