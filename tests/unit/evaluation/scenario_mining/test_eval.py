"""Scenario mining evaluation unit tests."""


import sys
if sys.stdout is None:
    sys.stdout = open('stdout.log', 'w')

from av2.evaluation.scenario_mining.eval import evaluate, load


def test_evaluate() -> None:
    """Test End-to-End Forecasting evaluation."""
    
    predictions = 'tests/unit/evaluation/scenario_mining/data/combined_predictions.pkl'
    ground_truth = '/home/crdavids/Trinity-Sync/av2-test/av2-api/tests/unit/evaluation/scenario_mining/data/combined_gt.pkl'

    objective_metric = 'HOTA'
    max_range_m = 100
    dataset_dir = None
    out = 'tests/unit/evaluation/scenario_mining/data/eval_results'

    predictions = load(predictions)
    ground_truth = load(ground_truth)

    evaluate(predictions, ground_truth, objective_metric, max_range_m, dataset_dir, out)

test_evaluate()



