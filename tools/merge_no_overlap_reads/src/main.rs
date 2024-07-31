use bio::io::fastq;

let fq: &'static [u8] = b"@id description\nACGT\n+\n!!!!\n";
let records = fastq::Reader::new(fq)
    .records()
    .map(|record| record.unwrap());
for record in records {
    assert!(record.check().is_ok())
}