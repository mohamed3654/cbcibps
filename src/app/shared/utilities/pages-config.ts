export let routesConfig = {
  'chatBot': {
    'name': 'chatbot',
    'route': '/chatbot',
    'module': './chat-bot/chat-bot.module#ChatBotModule',
    'chat': {
      'name': 'view',
      'route': '/view'
    },
    'registration': {
      'name': 'registration',
      'route': '/registration'
    }
  },
  'notFound': {
    'name': 'not-found',
    'route': '/not-found'
  }
};
