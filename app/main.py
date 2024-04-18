import decouple
import uvicorn
import sys

if __name__ == '__main__':
    decouple.config = decouple.Config(decouple.RepositoryEnv(sys.argv[1]))
    port = int(decouple.config('PORT'))
    sys.path.insert(0, '..')
    uvicorn.run("src.app:app", host="0.0.0.0", port=port, reload=True)