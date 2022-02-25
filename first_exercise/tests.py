from unittest import TestCase

from first_exercise.utils.tag_edit import remove_tags


class TestTagEdit(TestCase):
    def setUp(self) -> None:
        self.current_tags = [
            "ball",
            "power",
            "super",
            "job",
            "content"
        ]

    def test_remove_tags_function_with_special_characters(self):
        
        tags_to_remove = ["b-all", "p_ower", "j ob"]
        tags = remove_tags(self.current_tags, tags_to_remove)

        # b-all should be same as ball and should be removed
        # same with power
        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)
        self.assertNotIn("job", tags)

    def test_remove_tags_function_with_uppercases(self):
        tags_to_remove = ["BALL", "poWeR"]
        tags = remove_tags(self.current_tags, tags_to_remove)

        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)

    def test_add_tags_that_already_exists(self):
        #test the perservation of tags
        pass

    def test_add_tags_with_special_characters(self):
        pass

    def test_add_new_tags(self):
        pass

    def test_edit_tags_with_various_cases(self):
        pass

    

