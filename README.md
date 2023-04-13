# Random Instruction Generator (RIG)
RISC-V Random Instruction Generator Using Python


# Installing Spike Make a new directory for Spike:

	mkdir RISCV
	cd RISCV
	#Clone the repos for the RISCV GNU toolchain
	git clone --recursive https://github.com/riscv-collab/riscv-gnu-toolchain


Several standard packages are needed to build the toolchain.
On Ubuntu, executing the following command should suffice:
	
	sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev libnewlib-dev

#Build the toolchain

	cd riscv-gnu-toolchain 
	mkdir build 
	cd build 
	../configure --prefix=$RISCV 
	make

#Cloning for Riscv-pk & Riscv-isa-sim inside RISCV Dir

	git clone https://github.com/riscv/riscv-pk
	git clone https://github.com/riscv/riscv-isa-sim



Now, to build the Proxy Kernel

	cd ../riscv-pk 
	mkdir build 
	cd build 
	../configure --prefix=$RISCV--host=riscv64-unknown-elf 
	make 
	make install

Finally to build Spike

	cd ../riscv-isa-sim
	mkdir build 
	cd build 
	../configure --prefix=$RISCV --enable-histogram 
	make
	make install


Check if the installation is successful
Create a test.c, and enter the following codes:
 
	#include int main() 
	{ 
	printf("Hello world!\n");
	}


Then 

       test run:-
              riscv32-unknown-elf-gcc test.c
              /path/from/home/to/RISCV/riscv-isa-sim/build/spike --isa=RV32IMAC \
              /path/from/home/to/RISCV/riscv-pk/build/pk a.out

 disassemble:-
 
	riscv32-unknown-elf-objdump -d a.out &> asm.out


The command-line arguments to Spike can be listed with spike -h:

# usage: spike [host options] <target program> [target options]
Host Options:

              -p <n>             Simulate <n> processors
              -m <n>             Provide <n> MB of target memory
              -d                 Interactive debug mode
              -g                 Track histogram of PCs
              -h                 Print this help message
              --ic= <S>:<W>:<B>   Instantiate a cache model with S sets
              --dc= <S>:<W>:<B>     W ways, and B-byte blocks (with S and
              --l2= <S>:<W>:<B>     B both powers of 2).
              --extension=<name> Specify RoCC Extension
              --extlib=<name>    Shared library to load

sudo pip install xlwt xlrd




How to edit excel from Xls on Pyhon

sudo pip install xlwt xlrd
	loffice file.xls &

Python3 xl.py

riscv32-unknown-elf-gcc test.c

Refference:
http://acsa.ustc.edu.cn/ics/download/riscv/spike-tutorial-linux.pdf
	
https://www.francisz.cn/2020/07/22/riscv-simulator/
	
https://github.com/riscv-collab/riscv-gnu-toolchain
	
