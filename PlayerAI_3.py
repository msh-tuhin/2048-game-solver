from BaseAI_3 import BaseAI
import math


class PlayerAI(BaseAI):
    def getMove(self, grid):
        move, maxTile = self.maximize2(grid.clone(), 0, -1, 10000)
        # print(maxTile)
        return move

    def maximize(self, grid, depth, alpha, beta):
        new_grid = grid.clone()
        # print(new_grid.getMaxTile())
        if depth >= 4:
            return -1, 2*new_grid.getMaxTile()

        move, max_tile = -1, 0
        a_moves = new_grid.getAvailableMoves()
        for m in a_moves:
            new_grid.move(m)
            a, mt = self.minimize(new_grid.clone(), depth+1, alpha, beta)
            # print(mt)
            # mul = 0
            # if move == 1 or move == 3:
            #     mul = 100
            # elif move == 0:
            #     mul = 50
            # else:
            #     mul = 0
            # mt = mt + mul
            if mt > max_tile:
                move, max_tile = m, mt
                if mt >= beta:
                    break
                if mt > alpha:
                    alpha = mt
            new_grid = grid.clone()
        bal = grid.clone()
        flag = 0
        if bal.getMaxTile() == bal.map[3][3]:
            flag = 1
        av_cells = len(bal.getAvailableCells())
        bal.move(move)
        rem = len(bal.getAvailableCells())
        mul = 0
        if move == 1 or move == 3:
            mul = 100
        elif move == 0:
            mul = 50
        else:
            mul = 0
        return move, 2*max_tile + 4*(rem - av_cells) + 10 * flag + mul

    def minimize(self, grid, depth, alpha, beta):
        new_grid = grid.clone()
        # print(new_grid.getMaxTile())
        if depth >= 4:
            return 0, new_grid.getMaxTile()

        move, min_tile = -1, 10000
        a_moves = new_grid.getAvailableMoves()
        for m in a_moves:
            new_grid.move(m)
            rem = len(new_grid.getAvailableCells())
            a, mt = self.maximize(new_grid.clone(), depth+1, alpha, beta)
            # print(mt)
            mt = 2*mt + 40 * rem
            # mt = 1/rem
            if mt < min_tile:
                move, min_tile = m, mt
            if mt <= alpha:
                break
            if mt < beta:
                beta = mt
            new_grid = grid.clone()
        # bal = grid.clone()
        # av_cells = len(bal.getAvailableCells())
        # bal.move(move)
        # rem = len(bal.getAvailableCells())
        # return move, min_tile + 4 * (av_cells - rem)
        return move, min_tile



    def maximize2(self, grid, depth, alpha, beta):
        new_grid = grid.clone()
        if depth >= 5:
            return -1, self.eval(new_grid)

        move, max_tile = -1, -100000000
        a_moves = new_grid.getAvailableMoves()
        # if 2 in a_moves:
        #     a_moves.remove(2)
        for m in a_moves:
            new_grid.move(m)
            a, mt = self.minimize2(new_grid.clone(), depth+1, alpha, beta)
            if mt > max_tile:
                move, max_tile = m, mt
                if mt >= beta:
                    break
                if mt > alpha:
                    alpha = mt
            new_grid = grid.clone()
        return move, max_tile

    def minimize2(self, grid, depth, alpha, beta):
        new_grid = grid.clone()
        if depth >= 5:
            return 0, self.eval(new_grid)

        move, min_tile = -1, 10000000
        a_moves = new_grid.getAvailableMoves()
        # if 2 in a_moves:
        #     a_moves.remove(2)
        for m in a_moves:
            new_grid.move(m)
            a, mt = self.maximize2(new_grid.clone(), depth+1, alpha, beta)
            if mt < min_tile:
                move, min_tile = m, mt
            if mt <= alpha:
                break
            if mt < beta:
                beta = mt
            new_grid = grid.clone()
        return move, min_tile

    def eval(self, grid):
        max_tile = grid.getMaxTile()
        rem = len(grid.getAvailableCells())

        tiles = []
        for i in grid.map:
            for j in i:
                tiles.append(j)

        utility = 5*math.log(max_tile, 2)+ 6*rem + 6*self.check_adj(grid.clone())
        return utility

    def check_adj(self, grid):
        util = 0
        for x in range(grid.size):
            for y in range(grid.size):
                adj = self.get_adj(x, y)
                for i in adj:
                    if grid.map[x][y] == grid.map[i[0]][i[1]]:
                        u = math.log(grid.map[x][y], 2)
                        if u > util:
                            util = u
        return util
    def get_adj(self, x, y):
        adj = []
        for i in [x-1, x+1]:
            if i in range(4):
                adj.append((i, y))
        for j in [y-1, y+1]:
                if j in range(4):
                    adj.append((x, j))
        return adj

    def monotonicity(self, grid):
        pass
