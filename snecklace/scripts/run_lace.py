"""Run Lace to create the combined superTranscriptome"""

__author__ = "Sarah Hazell Pickering (sarah.pickering@anu.edu.au)"
__date__ = "2018-12-12"

#include: "cluster.py"

OUTPUT_DIR = "output_data/"
ST_OUTDIR = OUTPUT_DIR + "superT"

DATASET = config["dataset"]
#configfile: "necklace.json"

rule run_lace:
    version: "3.6"
    input:
        seqs = OUTPUT_DIR + "clustering/" + DATASET + "_sequences.fa",
        clusters = OUTPUT_DIR + "clustering/" + DATASET + ".clusters"
    conda: "../envs/lace.yml"
    threads: config["max_threads"]
    benchmark: ST_OUTDIR + "/10lace.times.tab"
    output:
        final = ST_OUTDIR + "/" + DATASET + "_SuperDuper.fa",
        working = directory("SuperFiles/")
    shell:
        "conda upgrade matplotlib -y; "
        "Lace.py --cores {threads} "
           # "--tidy "
            "--outputDir {output.working} "
            "{input.seqs} {input.clusters} ;"
        "mv {output.working}/SuperDuper.fasta {output.final} ;"
        "mv {output.working}/SuperDuper.gff {ST_OUTDIR}/SuperDuper.gff "
