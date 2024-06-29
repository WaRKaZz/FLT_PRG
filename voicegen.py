# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

import asyncio

import edge_tts

VOICE = "kk-KZ-AigulNeural"
OUTPUT_FOLDER = r"C:\Intel\PRJ\nomerin-aitashy\resources\voice_aigul"


async def main(text) -> None:
    """Main function"""
    communicator = edge_tts.Communicate(text, VOICE)
    await communicator.save(OUTPUT_FOLDER + f"\\{text.replace(' ', '')}.mp3")


if __name__ == "__main__":
    asyncio.run(main("  0  "))
    # for i in range(1001):
    #     asyncio.run(main(str(i)))
    # for i in range(10):
    #     asyncio.run(main(f"00{i}"))
    # for i in range(10, 100):
    #     asyncio.run(main(f"0 {i}"))
    # asyncio.run(main("плюс 7"))
