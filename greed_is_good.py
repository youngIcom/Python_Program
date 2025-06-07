def score(dice):
    #step 1: hitung kemunculan dari setiap angka
    counts = [0] * 7
    for die in dice:
        counts[die] += 1 #index tidak dipakai, index 1-6 untuk angka dadu

    total_score = 0

    #step 2: hitung score untuk triplet (3 dadu yang sama)
    triplet_scores = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}

    for number in range(1, 7):
        if counts[number] >= 3:
            total_score += triplet_scores[number]
            counts[number] -= 3

    #step 3: hitung skor untuk dadu individual 
    total_score += counts[1] * 100
    total_score += counts[5] * 50

    return total_score
            


# Testing
if __name__ == "__main__":

    print("=== GREED DICE GAME SCORER ===\n")
    
    # Test cases dari soal
    test_cases = [
        ([5, 1, 3, 4, 1], 250, "50 (for the 5) + 2 * 100 (for the 1s)"),
        ([1, 1, 1, 3, 1], 1100, "1000 (for three 1s) + 100 (for the other 1)"),
        ([2, 4, 4, 5, 4], 450, "400 (for three 4s) + 50 (for the 5)"),
        
        # Test cases tambahan
        ([1, 1, 1, 1, 1], 1200, "1000 (three 1s) + 200 (two individual 1s)"),
        ([6, 6, 6, 6, 6], 800, "600 (three 6s) + 0 (two individual 6s)"),
        ([5, 5, 5, 5, 5], 650, "500 (three 5s) + 100 (two individual 5s)"),
        ([1, 5, 1, 5, 1], 1100, "1000 (three 1s) + 100 (two individual 5s)"),
        ([2, 3, 4, 6, 2], 0, "No scoring combinations"),
        ([1, 2, 3, 4, 6], 100, "100 (one individual 1)"),
        ([5, 2, 3, 4, 6], 50, "50 (one individual 5)")
    ]

    # Test implementasi utama
    print("=== Testing Main Implementation ===")
    for i, (dice, expected, description) in enumerate(test_cases, 1):
        result = score(dice)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Dice: {dice}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Description: {description}")
        print()