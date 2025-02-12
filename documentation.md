# Project Report

Our goal is to make a model that can categorize websites based on their scraped data. The first problem is that we had non-labelled data. To train our model, we needed a labelled dataset. So we tried clustering websites together based on the keywords that were extracted from their content. But the clusters had too much noise. Our next approach was to use pre-trained models to categorize the text content scraped from websites. We tested two types of models:

1. **Fine-tuned models from Hugging Face**: These models are faster, smaller, and they require fewer resources. But the downside is that most of them are trained on some specific categories only, so they will not be able to categorize all the websites accurately.
2. **Open source LLM models from Ollama**: These are popular Large Language Models like Meta Llama, Deepseek V3, etc. These models are very accurate but they are very large in size and require very high resources.
   - *Ollama is a platform where quantized versions of LLM models are published.*

### We tested the following models for text classification from Hugging Face:
1. [Ali Mazhar Text Classification](https://huggingface.co/alimazhar-110/website_classification/blob/main/config.json) (only 15 categories available)
2. [Tiabet 2](https://huggingface.co/Tiabet/website_classification-finetuned-Tiabet-2/blob/main/config.json) (Only 5 categories available)
3. [Fine-Tuned Bart Model](https://huggingface.co/manimaranpa07/mnli_bart_text_classification_1_08th_march_margs/blob/main/config.json) (Overfitted on training model)
4. [Fine-Tuned Zero Shot](https://huggingface.co/MoritzLaurer/ModernBERT-large-zeroshot-v2.0/blob/main/config.json) (Overfitted on training model)

#### There are two types of models here:
1. The models that directly tell us the category only. The problem is that they are trained on different datasets and they have very limited categories. We cannot fine-tune them based on our requirements.
2. We define a list of categories, then the model evaluates the text content and tells us what is the most probable category of that content. These are called Zero Shot models For example:
```python
sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing']
classifier(sequence_to_classify, candidate_labels)
# Output:
# {'labels': ['travel', 'dancing', 'cooking'],
#  'scores': [0.9938651323318481, 0.0032737774308770895, 0.002861034357920289],
#  'sequence': 'one day I will see the world'}
```

At the end we decided to use [FaceBook Zero Shot Model](https://huggingface.co/facebook/bart-large-mnli).

The problem that we faced in this model is that it needs only cleaned text. Most of the websites have a huge paragraph about cookies or other non-relevant information in the scraped data. That makes the results less accurate. To overcome this, we used two methods. 
1. We used [Facebook Bart Large CNN](https://huggingface.co/facebook/bart-large-cnn) model. It is a text summarizer model. We first summarize the text and then give it to the classifier model. But it significantly increased the processing time and power.
2. Second solution was to extraxt keywords from the scraped data. This solution is more time efficient.

**We tested 1000 websites with the following categories. This was just our first iteration to check the initial accuracy.**

['Adult And Dating', 'Advertisements', 'Agriculture', 'Alcohol And Tobacco', 'Articles', 'Astrology', 'Automobiles And Transportation', 'Beauty', 'Biography', 'Blogs And Forums', 'Business', 'Cloudflare', 'Construction', 'Drugs', 'Ecommerce And Shopping', 'Education', 'Entertainment', 'Environment', 'Fashion', 'Finance', 'Food And Beverages', 'Gambling', 'Gaming', 'Government', 'Hacking', 'Health', 'Healthcare', 'Hobbies And Interests', 'Home And Garden', 'Intolerance And Hate', 'Jobs Search', 'Life', 'Logistics', 'Medicine', 'News', 'Non Governmental Organization', 'Parked Domain', 'Personal And Portfolio Website', 'Pets And Animals', 'Politics', 'Pornography', 'Real Estate And Property', 'Religious', 'Research', 'Restaurants And Dining', 'Search Engines', 'Security And Defense', 'Services and Repair', 'Social Media Networking', 'Society And Culture', 'Sports', 'Stock Market', 'Technology', 'Tourism', 'Unknown']

**After the first iteration, we manually categorised those 1000 websites and found out that the accuracy of the model was 67.5 percent. We also found following categories that were not present in our category list in our first iteration.** 

['Adult Entertainment', 'Architecture', 'Association', 'Auditons', 'AutoMobile', 'Automation', 'Automobiles', 'Business/Technology', 'Bussiness/Nonprofit', 'Coding', 'Constuction', 'Craked APPS', 'Crypto', 'Cybersecurity', 'Data Security', 'Dating', 'E- Commerce', 'E-Commerce', 'Ecommerce', 'Entertainment/Online Video Streaming', 'Escort Services', 'Food and Beverages', 'Hospitality', 'House Interior', 'INNOVATION/Reseach', 'Insurance', 'Jewellery', 'Legal', 'Lighting/Innovation', 'MARKETING', 'MARKETING/AUTOMATION', 'Manufacor', 'Manufactror', 'Manufactur', 'Manufacture', 'Manufacture and supplier', 'Marketing', 'Media/News', 'Music', 'NGO/Charity', 'News/ Blogs', 'ONLINE TOOLS STORE', 'Online Interview Preparation', 'Online Pdf Convertor', 'Online Store', 'Payments', 'Printing', 'Real Estate', 'Recycleing', 'Redirect To Google', 'Rewards And Coupens', 'SUPPLEMENTS', 'Social Media', 'Startup', 'Stationery Items', 'Techonology', 'Trust & Safety', 'UNCATEGORIZED', 'Visualization/Technology', 'WOOD', 'malicious', 'pharmaceutical']

**With this updated list, we will run the same websites again and test the accuracy.**

### AI Models