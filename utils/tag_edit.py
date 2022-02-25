

from typing import List, Optional


def edit_tags(current_tags: str, tags_to_add: Optional[List[str]] =None, tags_to_remove: Optional[List[str]] = None) -> str:
    """A Function to edit shopify arbitrary tags."""
    list_tag = current_tags.split(', ')
    str_to_add = ', '.join(tags_to_add)
    if tags_to_add:
        list_tag.append(str_to_add)
    if tags_to_remove:
        for tag in tags_to_remove:
            if tag in list_tag:
                list_tag.remove(tag)
    # convert to set to make the list unique
    # this wouldn't matter since orders dont mater
    set_tags = set(list_tag)
    tags = ', '.join(set_tags)
    return tags

current_tags = "bags, pillow"
tags_to_add = ["rubber"]
tags_to_remove = ["rubber"]
print(edit_tags(current_tags=current_tags, tags_to_add=tags_to_add, tags_to_remove=tags_to_remove))
