class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._depth_first_search(self.root, id)

    def _depth_first_search(self, node, id_to_find):
        if not node:
            return None

        if node.get("id") == id_to_find:
            return node

        for child in node.get("children", []):
            result = self._depth_first_search(child, id_to_find)
            if result:
                return result

        return None
