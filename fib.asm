.data 
	number: .word 10
	term1: .word 0
	term2: .word 1
.text
	lw $s0, number
	lw $t0, term1
	lw $t1, term2
	addi $t2, $t0, 1
	addi $t3, $t1, 1
	beq $s0, $t2, nis1
	beq $s0, $t3, nis2
	sle $s1, $s0, $zero
	beq $s1, $t1, nisnegative
	li $t2, 0	#fib3
	li $s2, 2	#term counter
	
	fib:
		add $t2, $t1, $t0
		add $t0, $t1, $zero
		add $t1, $t2, $zero
		addi $s2, $s2, 1
		bne $s2, $s0, fib
	li $v0, 1
	add $a0, $t1, $zero
	syscall
	lui $t5, 4097
	sw $a0, 32($t5)
	
	li $v0, 10
	syscall
	
	nisnegative:
		li $v0, 10
		syscall	
		
	nis1:
		li $v0, 1
		add $a0, $t0, $zero
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		
		li $v0, 10
		syscall	
	
	nis2:
		li $v0, 1
		add $a0, $t1, $zero
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		
		li $v0, 10
		syscall	
