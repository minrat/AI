#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph

class PageRank:

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

    def page_rank(self):
        #  先将图中没有出链的节点改为对所有节点都有出链
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size  # 构造公式中的(1−α)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node): 
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank) 
                page_rank[node] = rank
            print("This is NO.%s iteration" % (i + 1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("Finished in %s iterations!" % node)
        else:
            print("Finished out of 100 iterations!")
        return page_rank


if __name__ == '__main__':
    dg = digraph()
    node_lists = ["A", "B", "C", "D", "E"]
    dg.add_nodes(node_lists)
    dg.add_edge(("A", "B"))
    dg.add_edge(("A", "C"))
    dg.add_edge(("A", "D"))
    dg.add_edge(("B", "D"))
    dg.add_edge(("C", "E"))
    dg.add_edge(("D", "E"))
    dg.add_edge(("B", "E"))
    dg.add_edge(("E", "A"))

    pr = PageRank(dg)
    page_ranks = pr.page_rank()

    print("The final page rank is\n", page_ranks, "\n")
    print("***** Finally Check And Verify ***** \n")
    page_rank_dic={}
    for node in node_lists:
        P_node = page_ranks.get(node)
        page_rank_dic[node] = P_node
        print(node, " Has PageRank Is : ", P_node)
    out = 0
    for score in page_rank_dic:
        out += float(page_rank_dic[score])
    print("\nTotal Value is :", out)
