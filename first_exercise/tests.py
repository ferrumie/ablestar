from unittest import TestCase

from first_exercise.utils.tag_edit import add_tags, edit_tags, remove_tags


class TestTagEdit(TestCase):
    def setUp(self) -> None:
        self.current_tags = ["ball", "power", "super", "job", "content", "cold show"]
        self.passed_tags = "ball, power, super, job, Content, cold-show"

    def test_remove_tags_function_with_special_characters(self):

        tags_to_remove = ["b-all", "power", "j ob", "cold-show"]
        tags = remove_tags(self.current_tags, tags_to_remove)

        # b-all should be same as ball and should be removed
        # same with power
        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)
        self.assertNotIn("job", tags)
        self.assertNotIn("cold show", tags)

    def test_remove_tags_function_with_uppercases(self):
        tags_to_remove = ["BALL", "poWeR"]
        tags = remove_tags(self.current_tags, tags_to_remove)

        self.assertNotIn("ball", tags)
        self.assertNotIn("power", tags)

    def test_add_tags_that_already_exists(self):
        # test the perservation of tags

        tags_to_add = ["job"]
        tags = add_tags(self.current_tags, tags_to_add)

        self.assertEqual(len(self.current_tags), len(tags))
        # test that job is capitalized
        self.assertIn("JOB", self.current_tags)

        # test with different variations
        tags_to_add = ["Job"]
        tags = add_tags(self.current_tags, tags_to_add)

        self.assertEqual(len(self.current_tags), len(tags))

        # test with different variations
        tags_to_add = ["JO-b"]
        tags = add_tags(self.current_tags, tags_to_add)

        self.assertEqual(len(self.current_tags), len(tags))

        # test with different variations
        tags_to_add = ["cold-show"]
        tags = add_tags(self.current_tags, tags_to_add)

        self.assertEqual(len(self.current_tags), len(tags))

        # test with different variations
        tags_to_add = ["cold_show"]
        tags = add_tags(self.current_tags, tags_to_add)

        self.assertEqual(len(self.current_tags), len(tags))

    def test_add_new_tags(self):
        tags_to_add = ["code"]
        add_tags(self.current_tags, tags_to_add)

        self.assertIn("code", self.current_tags)

        # add tags

    def test_edit_tags_with_various_cases(self):
        # remove an added tag
        tags_to_add = ["title-snow"]
        tags_to_remove = ["title snow"]

        tags = edit_tags(current_tags=self.passed_tags, tags_to_add=tags_to_add, tags_to_remove=tags_to_remove)
        self.assertNotIn("title-snow", tags)

        # case of tags should be preserved
        tags_to_add = ["contents"]
        tags = edit_tags(current_tags=self.passed_tags, tags_to_add=tags_to_add)
        self.assertIn("Content", tags)

        # special characters
        tags_to_remove = ["cold show"]
        tags = edit_tags(current_tags=self.passed_tags, tags_to_remove=tags_to_remove)
        self.assertNotIn("cold-show", tags)

        tags_to_add = ["cold_show"]
        tags = edit_tags(current_tags=self.passed_tags, tags_to_add=tags_to_add)
        # capitalization of the new tag should be added
        self.assertIn("COLD_SHOW", tags)
        self.assertNotIn("cold-show", tags)
