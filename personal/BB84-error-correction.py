import numpy as np

def correct_errors(alice_key, bob_key, block_size=4):
    """
    A simplified Error Correction (Information Reconciliation) step.
    Alice and Bob compare block parities and Bob fixes bits.
    """
    corrected_bob_key = bob_key.copy()
    
    for i in range(0, len(alice_key), block_size):
        # Define the current block
        end = min(i + block_size, len(alice_key))
        alice_block = alice_key[i:end]
        bob_block = corrected_bob_key[i:end]
        
        # Alice and Bob compute parity (0 if even number of 1s, 1 if odd)
        alice_parity = np.sum(alice_block) % 2
        bob_parity = np.sum(bob_block) % 2
        
        # If parities differ, there is an error in this block
        if alice_parity != bob_parity:
            # In a real protocol, they would do a binary search.
            # Here, Bob 'finds' and fixes the first mismatch in the block.
            for j in range(i, end):
                if alice_key[j] != corrected_bob_key[j]:
                    corrected_bob_key[j] = alice_key[j]
                    break # Fix one bit and move to next block
                    
    return corrected_bob_key

def simulate_bb84_full(num_bits=100, eve_present=True):
    # 1. Alice's Data
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.randint(2, size=num_bits)

    # 2. Transmission (with optional Eve)
    current_bits = alice_bits.copy()
    if eve_present:
        eve_bases = np.random.randint(2, size=num_bits)
        for i in range(num_bits):
            if eve_bases[i] != alice_bases[i]:
                current_bits[i] = np.random.randint(2)

    # 3. Bob's Measurement
    bob_bases = np.random.randint(2, size=num_bits)
    bob_bits = np.array([current_bits[i] if bob_bases[i] == alice_bases[i] else np.random.randint(2) for i in range(num_bits)])

    # 4. Sifting
    mask = (alice_bases == bob_bases)
    alice_sifted = alice_bits[mask]
    bob_sifted = bob_bits[mask]

    # 5. Pre-Correction Analysis
    initial_errors = np.sum(alice_sifted != bob_sifted)
    print(f"--- Sifting Complete ---")
    print(f"Sifted Key Length: {len(alice_sifted)}")
    print(f"Errors Found: {initial_errors}")

    # 6. Error Correction (The new step!)
    if initial_errors > 0:
        print("\nPerforming Error Correction...")
        bob_final_key = correct_errors(alice_sifted, bob_sifted)
    else:
        bob_final_key = bob_sifted

    # 7. Final Verification
    final_errors = np.sum(alice_sifted != bob_final_key)
    print(f"Final Errors after Correction: {final_errors}")
    
    if final_errors == 0:
        print("SUCCESS: Keys are now synchronized.")
    else:
        print("FAILURE: Too many errors to fix. Eve's interference was too high.")

simulate_bb84_full(100, eve_present=True)
