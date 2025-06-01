from unidecode import unidecode
from django.db import models


##### CUSTOM LOOKUPS #####
class AccentCaseInsensitiveContains(models.Lookup):
    lookup_name = "acicontains"

    def as_sql(self, compiler, connection):
        lhs, _ = self.process_lhs(compiler, connection)
        _, rhs_params = self.process_rhs(compiler, connection)

        # Normalize and wrap RHS param with %
        rhs_value = rhs_params[0]
        rhs_normalized = f"%{unidecode(rhs_value)}%"

        return f"LOWER({lhs}) LIKE %s", [rhs_normalized]


models.Field.register_lookup(AccentCaseInsensitiveContains)


##### MODELS #####
class AccentInsensitiveModel(models.Model):
    """
    Abstract model to apply accent insensitive lookups.
    """

    search_field = models.CharField(255, blank=True)

    class Meta:
        abstract = True


class Film(AccentInsensitiveModel):
    rank = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField("Actor", related_name="films")

    def __str__(self):
        return self.title


class Actor(AccentInsensitiveModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
