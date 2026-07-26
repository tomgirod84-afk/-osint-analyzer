export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url)
    const target = url.searchParams.get('url')

    if (!target) {
      return new Response(JSON.stringify({error: 'Missing ?url= parameter'}), {
        status: 400,
        headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
      })
    }

    if (!target.startsWith('https://opensky-network.org/')) {
      return new Response(JSON.stringify({error: 'Only opensky-network.org allowed'}), {
        status: 403,
        headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
      })
    }

    const apiResponse = await fetch(target, {
      headers: {'Accept': 'application/json'}
    })

    const body = await apiResponse.text()

    return new Response(body, {
      status: apiResponse.status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=10'
      }
    })
  }
}
