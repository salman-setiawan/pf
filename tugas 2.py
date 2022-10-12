import collections
 
Uno = collections.namedtuple('Uno', ['rank', 'color'])
 
class UnoCard:
    ranks = [str(n) for n in range(1, 10)] + ['🔁', '🔞', '+2']
    colors = '🟥 🟨 🟩 🟦'.split()
 
    def __init__(self):
        self._unos = [Uno(rank, color) for rank in self.ranks for color in self.colors]
        for i in range(0,4):
            self._unos.append(Uno('+4', '⬛️'))
            self._unos.append(Uno('🌈', '⬛️'))
 
    def __len__(self):
        return len(self._unos)
 
    def __getitem__(self, position):
        return self._unos[position]
 
    def returnAll(self):
        return self._unos
 
run = UnoCard
for i in run().returnAll():
    print(i)
