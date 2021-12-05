class Place:
    def __init__(self, holding):
        self.holding = holding

class ArcBase:
    def __init__(self, place, amount=1):
        self.place = place
        self.amount = amount
        
class Out(ArcBase):
    def trigger(self):
        self.place.holding -= self.amount
    def non_blocking(self):
        return self.place.holding >= self.amount 
        
class In(ArcBase):  
    def trigger(self):
        self.place.holding += self.amount
        
class Transition:
    def __init__(self, out_arcs, in_arcs):
        self.out_arcs = set(out_arcs)
        self.arcs = self.out_arcs.union(in_arcs)
    def fire(self):
        not_blocked = all(arc.non_blocking() for arc in self.out_arcs) 
        if not_blocked:
            for arc in self.arcs:
                arc.trigger()
        return not_blocked 




