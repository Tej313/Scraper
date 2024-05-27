export PYTHONPATH="/Users/tej/Desktop/hgj/Scraper:$PYTHONPATH"

from Scraper.beautiful_soup import extract_phrases, fetch_and_parse_jobs, get_top_skills

class TestBeautifulSoup(unittest.TestCase):

    def test_extract_phrases(self):
        text = "Python developer"
        expected = ["python developer"]
        self.assertEqual(extract_phrases(text), expected)

    def test_fetch_and_parse_jobs(self):
        url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
        jobs = fetch_and_parse_jobs(url)
        self.assertGreater(len(jobs), 0)

    def test_get_top_skills(self):
        jobs = [
            {'skills': 'python developer'},
            {'skills': 'data scientist'}
        ]
        top_skills = get_top_skills(jobs)
        self.assertGreater(len(top_skills), 0)

if __name__ == '__main__':
    unittest.main()
