import numpy as np

def simulate_bb84(num_bits=20):
    print(f"--- Simulating BB84 with {num_bits} photons ---\n")

    # 1. Alice generates random bits and random bases
    # 0 = Rectilinear (+), 1 = Diagonal (x)
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.randint(2, size=num_bits)

    # 2. Bob chooses random bases to measure Alice's photons
    bob_bases = np.random.randint(2, size=num_bits)
    
    # Bob's measurement results
    bob_bits = []
    for i in range(num_bits):
        if alice_bases[i] == bob_bases[i]:
            # Same basis: Bob gets the bit Alice sent
            bob_bits.append(alice_bits[i])
        else:
            # Different basis: Bob gets a random result (quantum noise)
            bob_bits.append(np.random.randint(2))
    bob_bits = np.array(bob_bits)

    # 3. Sifting: Alice and Bob compare bases (publicly)
    # They keep bits only where their bases matched
    agreement_mask = (alice_bases == bob_bases)
    final_key_alice = alice_bits[agreement_mask]
    final_key_bob = bob_bits[agreement_mask]

    # --- Display Results ---
    print(f"Alice's Bits:  {alice_bits}")
    print(f"Alice's Bases: {alice_bases} (0=+, 1=x)")
    print(f"Bob's Bases:   {bob_bases} (0=+, 1=x)")
    print(f"Matches:       {agreement_mask.astype(int)}")
    print("-" * 40)
    print(f"Final Key (Alice): {final_key_alice}")
    print(f"Final Key (Bob):   {final_key_bob}")
    
    # Verification
    if np.array_equal(final_key_alice, final_key_bob):
        print("\nSuccess! The keys match perfectly.")
    else:
        print("\nError! The keys do not match (could be an eavesdropper).")

# Run the demo
simulate_bb84(20)

