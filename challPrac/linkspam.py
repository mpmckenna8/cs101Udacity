# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can
# collude with each other to improve their page ranks.  We consider
# A->B a reciprocal link if there is a link path from B to A of length
# equal to or below the collusion level, k.  The length of a link path
# is the number of links which are taken to travel from one page to the
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A,
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link
# A->B, which includes one link and so is of length 1. (it requires
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to
#   - take an extra input k, which is a non-negative integer, and
#   - exclude reciprocal links of length up to and including k from
#     helping the page rank.

def matched(page, arr):
    if page in arr:
        return True
    return False

def isspam(graph, area, page, k):
    print 'fing area ' + area
    print page
    print graph
    if k == 0:
        for i in graph[area]:
            if area == i and page == i:
                return True
        #if done == True:
        return False
    elif k > 0:
        if page == area:
            return True

        for i in graph[page]:
            print 'do ' + i + ' page is ' + page
            print i == page
            if area == i:
                return True
            if k >1:
                if area in graph[i]:
                    return True
                    print 'somehow true'
                else:
                    print 'dont know what to do here'
                    print k
                    if k > 1:
                        for g in graph[i]:
                            print 'and ght e g is ' + g
                            if area == g:
                                return True
                            if k >2:
                                for o in graph[g]:
                                    if area == o:
                                        return True
                                    if k >3:
                                        for q in graph[o]:
                                            if area == q:
                                                return True
                                        








        return False






    else:
        return False
#    print "False"
    return False


'''
def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        ker = 0
        for page in graph:
            print page
            ker = ker + 1

            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if page not in g[page]:
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks
'''

def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    onk = 0
    print 'ranks at first'
    print ranks

    spamg = {}
    links = {}

    for c in graph:
        print 'gaaa ' + c
        spamg[c] = c
        spamg[c] = []


        for a in graph[c]:
            print 'grrr ' + a
            print isspam(graph, a, c, k)
            namesp = a +"to" + c
            links[namesp] = isspam(graph, c, a, k)
            print namesp + ' area and page ' + c + " " + a
            print links

            spamg[c].append({a:isspam(graph, a, c, k)})

        print links


    for i in range(0, numloops):
        newranks = {}

        for page in graph:
            print page

            newrank = (1 - d) / npages
#            print newrank


            for node in graph:
                #print 'and the node is'
                #print node
                if page in graph[node]:
                    banker = page + "to" + node
                    if links[banker]:
                        print 'spam alert'
                    else:

                        newrank = newrank + d * (ranks[node]/len(graph[node]))

            newranks[page] = newrank
            #print newranks
        ranks = newranks
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}
#g = {'a': [ 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}

g = {'a': ['a', 'b', 'c'], 'c': ['d'], 'b': ['a'], 'e': ['b'], 'd': ['a', 'e']}

print compute_ranks(g, 3)
#
#`0.0848` for `b` i

print compute_ranks(g, 4)
#
