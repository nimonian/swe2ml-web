import chokidar from 'chokidar'
import { exec } from 'child_process'
import { fileURLToPath } from 'url'

const dir = fileURLToPath(new URL('.', import.meta.url))

const watcher = chokidar.watch('.', {
  ignored: (path, stats) => stats?.isFile() && !path.endsWith('.tex')
})

const handleChange = () => {
  exec(`make -C ${dir}`, (error, _stdout, stderr) => {
    if (error) {
      console.error(`${error}`)
      return
    }
    console.error(stderr)
  })
}

watcher.on('change', handleChange)
watcher.on('add', handleChange)
watcher.on('error', console.error)
