# PronouncUR

This tool generates a pronunciation dictionary from a list of Urdu words in a form, suitable for use with a speech recognizer, such as [CMUSphinx](https://cmusphinx.github.io/), [KALDI](http://kaldi-asr.org/) and text-to-speech system, such as [MaryTTS](http://mary.dfki.de/).

Read my lips - this tool works only for Urdu. This means this tool only support Urdu graphemes (letters).

Live Demo: http://lextool.csalt.itu.edu.pk

# Requirements

This tool requires [TensorFlow](https://www.tensorflow.org/) and [Sequence-to-Sequence G2P toolkit](https://github.com/cmusphinx/g2p-seq2seq). Please see [requirements.txt](https://github.com/harisbinzia/PronouncUR/blob/master/requirements.txt) for details.

# Model

A pretrained model (2-layer LSTM with 512 hidden units) is [available for download](https://github.com/harisbinzia/PronouncUR/tree/master/itudict). The model is trained on a handcrafted expert lexicon of around 39,000 words.

# References

If you use this tool in any of your work, please cite below paper.

## [PronouncUR: An Urdu Pronunciation Lexicon Generator](https://arxiv.org/abs/1801.00409)

# License

See the [LICENSE](https://github.com/harisbinzia/PronouncUR/blob/master/LICENSE) file.
