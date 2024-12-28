.data
	first: .word 1
	second: .word 4
	third: .word 4
.text
	lw $s0, first
	lw $s1, second
	lw $s2, third
	
	mul $t0, $s1, $s1	#b*b
	mul $t1, $s0, $s2	#a*c
	mul $t1, $t1, 4	#4*a*c
	sub $t0, $t0, $t1
	beq $t0, $zero, equal_roots
	slt $t1, $t0, $zero
	beq $t1, 1, no_roots
	
	real_roots:
		li $v0, 1	
		li $a0, 2	#save number of roots
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		j exit
	
	equal_roots:
		li $v0, 1	#to print
		li $a0, 1	#save number of roots
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		j exit
	
	exit:			#exit out
		li $v0, 10
		syscall
	
	no_roots:
		li $v0, 1	#to print
		li $a0, 0	#save number of roots
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		j exit
