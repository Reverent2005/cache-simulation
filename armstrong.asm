.data
	number: .word 121
.text
	lw $s0,	number	#store the number
	add $t0, $s0, $zero	#copy the number for manipulation
	
	li $s1, 0	#stores the sum
	
	li $t1, 0
	
	count_digits:
		li $t4, 10
		div $t0, $t4
		mflo $t0
		addi $t1, $t1, 1
		bne $t0, $zero, count_digits
	
	add $s2, $t1, $zero	#number of digits
	add $t0,$s0, $zero	#again for manipulation
	
	calculate_sum:
		li $t4, 10
		div $t0, $t4
		mfhi $t1 #storing remainder
		mflo $t0
		add $t2, $s2, $zero
		li $t3, 1
		power:
			mul $t3, $t3, $t1 
			subi $t2, $t2, 1
			bne $t2, $zero, power
		add $s1, $s1, $t3
		bne $t0, $zero, calculate_sum
		
	beq $s0, $s1, is_armstrong
	
	not_armstrong:
		li $v0, 1
		li $a0, 0
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		j exit
		
	is_armstrong:
		li $v0, 1
		li $a0, 1
		syscall
		lui $t5, 4097
		sw $a0, 32($t5)
		j exit
		
	exit:
		li $v0, 10
		syscall
		
		
		
			
			
			
		
