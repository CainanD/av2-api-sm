"""Constants for tracking challenge."""

from typing import Final

from av2.evaluation.scenario_mining import ScenarioMiningCategories

SUBMETRIC_TO_METRIC_CLASS_NAME: Final = {
    "MOTA": "CLEAR",
    "HOTA": "HOTA",
}

AV2_CATEGORIES: Final = tuple(x.value for x in ScenarioMiningCategories)
