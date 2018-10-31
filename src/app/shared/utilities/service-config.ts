const baseURL = 'http://localhost:5000';

export const API_URLS = {
  PROCESS_QUESTION: (question) => `${baseURL}/process_question?question=' + ${question}`
};

