import GameManager_3
import PlayerAI_3
import time
start = time.time()
for i in range(5):
    GameManager_3.main()

print(time.time() - start)

# p = PlayerAI_3.PlayerAI()
# a=p.get_adj(3,1)
# print(a)
# p.get_adj(0,0)
# print(a)

