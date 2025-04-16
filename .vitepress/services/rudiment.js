const rudimentService = {
  base: 'http://127.0.0.1:5001/rudiments/',

  async get(id) {
    const url = new URL(id, this.base)
    const res = await fetch(url.toString())
    const data = await res.json()
    console.log(data)
    return data
  }
}

export default rudimentService
