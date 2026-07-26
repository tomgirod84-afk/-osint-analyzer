// Cloudflare Worker - CORS Proxy for OpenSky Network API
// Deploy: https://workers.cloudflare.com (gratuit, 100k req/jour)
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  const target = url.searchParams.get('url')

  if (!target) {
    return new Response(JSON.stringify({error: 'Missing ?url= parameter'}), {
      status: 400,
      headers: {'Content-Type': 'application/json'}
    })
  }

  // Only allow OpenSky requests
  if (!target.startsWith('https://opensky-network.org/')) {
    return new Response(JSON.stringify({error: 'Only opensky-network.org allowed'}), {
      status: 403,
      headers: {'Content-Type': 'application/json'}
    })
  }

  const apiResponse = await fetch(target, {
    headers: {'Accept': 'application/json'},
    cf: {cacheTtl: 10}
  })

  const body = await apiResponse.text()

  return new Response(body, {
    status: apiResponse.status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET',
      'Cache-Control': 'public, max-age=10'
    }
  })
}
