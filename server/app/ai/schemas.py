from pydantic import BaseModel, Field
from datetime import date

CURRENT_YEAR = date.today().year



class ParsedRequest(BaseModel): 
    # TODO: validate each tag against the genre list (validator, once William's tag list exists)
    tags: list[str] = Field(default_factory=list, max_length=5)

    # TODO: validate each tag against the genre list (validator, once William's tag list exists)
    exclude_tags: list[str] = Field(default_factory=list, max_length=5)

    mood: str | None = Field(default=None, max_length=50)

    mood_tags: list[str] = Field(default_factory=list, max_length=3)

    # TODO: validate year min is not greater than year max
    year_min: int | None = Field(default=None, ge=1900, le=CURRENT_YEAR)

    year_max: int | None = Field(default=None, ge=1900, le=CURRENT_YEAR)

    seed_artists: list[str] = Field(default_factory=list, max_length=5)

    unsupported: list[str] = Field(default_factory=list, max_length=5)