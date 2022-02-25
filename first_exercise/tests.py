from unittest import TestCase

from first_exercise.utils.tag_edit import remove_tags


class TestTagEdit(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_remove_tags_function_with_special_characters(self):
        current_tags = [
            "ball",
            "power",
            "super",
            "job",
            "content"
        ]
        tags_to_remove = ["b-all", "p_ower"]
        tags = remove_tags(current_tags, tags_to_remove)

        # b-all should be same as ball and should be removed
        # same with power
        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)

    def test_remove_tags_function_with_uppercases(self):
        current_tags = [
            "ball",
            "power",
            "super",
            "job",
            "content"
        ]
        tags_to_remove = ["BALL", "poWeR"]
        tags = remove_tags(current_tags, tags_to_remove)

        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)

