import re
from typing import List, Optional


def remove_tags(current_tags_list: List[str], tags_to_remove: List[str]) -> List[str]:
    """The logic to remove tags, this takes care of lowercases and special chars."""
    lowercase_tags = [tags.lower() for tags in tags_to_remove]
    flushed_tags_to_remove = [re.sub("[-_ ]", "", tags) for tags in lowercase_tags]
    complete_tags_list = []

    for tag in current_tags_list:
        flushed_tag = re.sub("[-_ ]", "", tag)
        if flushed_tag.lower() not in flushed_tags_to_remove:
            complete_tags_list.append(tag)
    return complete_tags_list


def add_tags(current_tags_list: List[str], tags_to_add: List[str]) -> List[str]:
    """The logic to remove tags, this takes care of lowercases and special chars."""
    lowercase_tags = [tags.lower() for tags in current_tags_list]
    flushed_tags = [re.sub("[-_ ]", "", tags) for tags in lowercase_tags]
    for tag in tags_to_add:
        flushed_tag_to_add = re.sub("[-_ ]", "", tag)
        if flushed_tag_to_add.lower() not in flushed_tags:
            current_tags_list.append(tag)
        if flushed_tag_to_add.lower() in flushed_tags:
            for current_tag in current_tags_list:
                flushed_tag = re.sub("[-_ ]", "", current_tag)
                if flushed_tag.lower() == flushed_tag_to_add.lower():
                    current_tags_list.remove(current_tag)
            current_tags_list.append(tag.upper())
    return current_tags_list


def edit_tags(
    current_tags: str, tags_to_add: Optional[List[str]] = None, tags_to_remove: Optional[List[str]] = None
) -> str:
    """A Function to edit shopify arbitrary tags."""
    list_tags = current_tags.split(', ')
    if tags_to_add:
        list_tags = add_tags(list_tags, tags_to_add)
    if tags_to_remove:
        list_tags = remove_tags(list_tags, tags_to_remove)
    set_tags = set(list_tags)
    tags = ', '.join(set_tags)
    return tags
