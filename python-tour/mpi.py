from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # número de proceso actual
size = comm.Get_size()  # número de ranks

# print(rank, size)

"""
if rank == 0:
    data = [i for i in range(1, 7)]
    comm.send(data, dest=1, tag=1)
elif rank == 1:
    data = comm.recv(source=0, tag=1)
    print(data)
"""

"""
data = None
if rank == 0:
    data = [1, 2, 3, 4]

data = comm.bcast(data, root=0)
print(f"{rank}/{size}", data)
"""

"""
data = None
if rank == 0:
    data = [1, 2, 3, 4]

data = comm.scatter(data, root=0) # divide entre el número de procesos
print(f"{rank}/{size}", data)
"""


data = None
if rank == 0:
    data = [12, 13, 14, 15]

data = comm.scatter(data, root=0)
print(f"{rank}/{size}", data)

data *= 2
data = comm.gather(data, root=0)
if rank == 0:
    print(data)
