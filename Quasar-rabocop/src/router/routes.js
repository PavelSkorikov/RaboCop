
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/register', component: () => import('components/register.vue') },
      { path: '/login', component: () => import('components/login.vue') },
      { path: '/question', component: () => import('components/question.vue') },
      { path: '/desktop', component: () => import('components/desktop.vue') }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
