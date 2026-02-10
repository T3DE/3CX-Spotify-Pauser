import asyncio
from winrt.windows.media.control import (
    GlobalSystemMediaTransportControlsSessionManager
)

async def pause_spotify():
    manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
    session = manager.get_current_session()

    if not session:
        print("No active media session")
        return

    info = await session.try_get_media_properties_async()
    source = session.source_app_user_model_id.lower()

    if "spotify" not in source:
        print("Active session is not Spotify")
        return

    await session.try_pause_async()
    print("Spotify paused")

asyncio.run(pause_spotify())
