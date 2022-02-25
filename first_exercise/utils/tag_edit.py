

from typing import List, Optional
import re

def remove_tags(current_tags_list: List[str], tags_to_remove: List[str]) -> List[str]:
    """The logic to remove tags, this takes care of lowercases and special chars."""
    lowercase_tags = [tags.lower() for tags in current_tags_list]
    flushed_tags = [re.sub("[-_ ]", "",  tags) for tags in lowercase_tags]
    flushed_tags_to_remove = [re.sub("[-_ ]", "",  tags) for tags in tags_to_remove]
    print(flushed_tags_to_remove)


    # replace dash and underscrores with space
    for tag in flushed_tags_to_remove:
        if tag.lower() in flushed_tags:
            flushed_tags.remove(tag)
    return flushed_tags

def edit_tags(current_tags: str, tags_to_add: Optional[List[str]] =None, tags_to_remove: Optional[List[str]] = None) -> str:
    """A Function to edit shopify arbitrary tags."""
    list_tag = current_tags.split(', ')
    str_to_add = ', '.join(tags_to_add)
    if tags_to_add:
        list_tag.append(str_to_add)
    if tags_to_remove:
        list_tag = remove_tags(list_tag, tags_to_remove)
    # convert to set to make the list unique
    # this wouldn't matter since orders dont mater
    set_tags = set(list_tag)
    tags = ', '.join(set_tags)
    return tags

current_tags = "bags, pillow"
tags_to_add = ["RuBber bird"]
tags_to_remove = ["rubbe r"]
print(edit_tags(current_tags=current_tags, tags_to_add=tags_to_add, tags_to_remove=tags_to_remove))
