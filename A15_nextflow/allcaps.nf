#!/usr/bin/env nextflow

workflow {
    inputChannel = Channel.value(params.input_string) // Input from parameter
    uppercase(inputChannel)
}

process uppercase {
    input:
    val input_string // Input value

    output:
    file "result.txt" 

    publishDir ".", mode: "copy" // Publish the result to the current directory

    script:
    """
    echo '${input_string}' | awk '{ print toupper(\$0) }' > result.txt
    """
}

