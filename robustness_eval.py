"""
Prompt-robustness eval: measures how much MCQ accuracy shifts
under trivial reformatting (answer-order shuffling).
"""

from inspect_ai import Task, task
from inspect_ai.dataset import Sample, csv_dataset
from inspect_ai.solver import multiple_choice
from inspect_ai.scorer import choice


# --- Convert a dataset record into an Inspect Sample -----------------
def record_to_sample(record: dict) -> Sample:
    """
    Expects columns: question, A, B, C, D, answer
    where `answer` is a letter like "A".
    """
    return Sample(
        input=record["question"],
        choices=[record["A"], record["B"], record["C"], record["D"]],
        target=record["answer"],
    )


def load_dataset(shuffle_choices: bool):
    return csv_dataset(
        "questions.csv",
        sample_fields=record_to_sample,
        shuffle_choices=shuffle_choices,  # this is the key manipulation
    )


# --- Baseline: options in their original order ----------------------
@task
def mcq_baseline():
    return Task(
        dataset=load_dataset(shuffle_choices=False),
        solver=multiple_choice(),
        scorer=choice(),
    )


# --- Variant: options shuffled -------------------------------------
@task
def mcq_shuffled():
    return Task(
        dataset=load_dataset(shuffle_choices=True),
        solver=multiple_choice(),
        scorer=choice(),
    )
