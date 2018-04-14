import xml.etree.cElementTree as ET


class Links:

    def __init__(self, source, target, edgeId):
        # continue from here for making Link objects, not used so far
        self.source = source
        self.target = target

        self.edgeId = edgeId


class TopologyVisualiser:

    def __init__(self, nodes, links={}):
        # Links need to be added
        self.nodes = nodes
        self.links = links

    def setNode(self, node):
        Node = ET.Element("node", id=self.nodes.get(node))
        return Node

    # def setLink( self, source, target, edgeId ):

    # link = Links( source, target, edgeId )
    # self.edges[link.edgeId]=link

    def buildElements(self):
        graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
        graphml.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        graphml.set("xsi:schemaLocation",
                    "http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")

        nodeKey = ET.SubElement(graphml, "key", id="d0")
        nodeKey.set("for", "node")
        nodeKey.set("yfiles.type", "nodegraphics")

        edgeKey = ET.SubElement(graphml, "key", id="d1")
        edgeKey.set("for", "edge")
        edgeKey.set("yfiles.type", "edgegraphics")

        graph = ET.SubElement(graphml, "graph", id="G")
        graph.set("edgedefault", "undirected")
        # node = ET.SubElement(graph ,"node", id="n0")
        # node = ET.SubElement(graph ,"node", id="n1")
        # node = ET.SubElement(graph ,"node", id="n2")

        for node in self.nodes:
            Node = self.setNode(node)
            graph.append(Node)

        link = ET.SubElement(graph, "edge", id="e0")
        link.set("source", "n0")
        link.set("target", "n1")
        link = ET.SubElement(graph, "edge", id="e1")
        link.set("source", "n0")
        link.set("target", "n2")

        Tree = ET.ElementTree(graphml)
        Tree.write("test.graphml", encoding="UTF-8")


# Remove this
if __name__ == '__main__':
    obj = TopologyVisualiser(nodes={"node1": "n0", "node2": "n1", "node3": "n2"})
    obj.buildElements()
