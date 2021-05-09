import fitz
import pyttsx3

doc = fitz.open("book2.pdf", filetype="pdf")
text = []
for page_number in range(5, doc.pageCount):
    page = doc.loadPage(page_number)
    page_text = '\n'.join(block[4] for block in page.getTextBlocks())
    text.append(page_text)
final_text = '\n'.join(text)

speaker = pyttsx3.init()
speaker.say(final_text)
speaker.runAndWait()
