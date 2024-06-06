from django.shortcuts import render
from Bio.Seq import Seq
import re

def get_sequences(request):
    if request.method == 'POST':
        dna_sequence = request.POST.get('''dna_sequence''')
        dna_sequence = re.sub(r'\s+', '', dna_sequence)
        dna_seq = Seq(dna_sequence)
        protein_seq = dna_seq.translate()
        rna_seq = dna_seq.back_transcribe()
        return render(request, 'results.html', {'protein_seq': protein_seq, 'rna_seq': rna_seq})
    return render(request, 'index.html')