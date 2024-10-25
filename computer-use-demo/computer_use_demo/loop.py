# Core function: sampling_loop
async def sampling_loop(
    model: str,
    provider: APIProvider,
    system_prompt_suffix: str,
    messages: list[BetaMessageParam],
    output_callback: Callable[[BetaContentBlockParam], None],
    tool_output_callback: Callable[[ToolResult, str], None],
    api_response_callback: Callable[[httpx.Request, httpx.Response | object | None, Exception | None], None],
    api_key: str,
    only_n_most_recent_images: int | None = None,
    max_tokens: int = 4096,
):
    """
    Main loop that handles the interaction between the assistant and computer tools. Key responsibilities:
    - Initializes tool collection (Computer, Bash, Edit tools)
    - Sets up system prompt with environment details
    - Manages API client based on provider (Anthropic, Vertex, Bedrock)
    - Handles prompt caching for optimization
    - Processes messages and tool responses in a continuous loop
    - Manages image history truncation
    - Handles API errors and callbacks
    
    Flow:
    1. Sets up tools and system prompt
    2. Configures API client and features based on provider
    3. Applies prompt caching if enabled
    4. Handles image history management
    5. Makes API call with current context
    6. Processes response and executes any tool commands
    7. Continues loop if tool commands were executed
    """

# Core function: _maybe_filter_to_n_most_recent_images
def _maybe_filter_to_n_most_recent_images(
    messages: list[BetaMessageParam],
    images_to_keep: int,
    min_removal_threshold: int,
):
    """
    Manages the image history in the conversation by removing older images while preserving recent ones.
    Key features:
    - Optimizes context window usage by removing old screenshots
    - Maintains cache efficiency by removing images in chunks
    - Preserves most recent and relevant images
    
    Algorithm:
    1. Counts total images in tool results
    2. Calculates images to remove based on keep limit
    3. Rounds removal count to threshold for cache efficiency
    4. Processes tool results in order, removing old images
    5. Preserves specified number of most recent images
    """

# Core function: _inject_prompt_caching
def _inject_prompt_caching(messages: list[BetaMessageParam]):
    """
    Implements prompt caching optimization by setting cache breakpoints.
    Key features:
    - Maintains 3 most recent conversation turns in cache
    - Reserves one cache breakpoint for tools/system prompt
    - Optimizes API performance by reducing redundant processing
    
    Strategy:
    1. Works backwards through messages
    2. Sets cache breakpoints for last 3 turns
    3. Removes older cache controls
    4. Balances cache efficiency with conversation coherence
    """

# Core function: _make_api_tool_result
def _make_api_tool_result(result: ToolResult, tool_use_id: str) -> BetaToolResultBlockParam:
    """
    Converts internal tool results into API-compatible format.
    Handles:
    - Text output formatting
    - Error state management
    - Image data processing
    - System message integration
    
    Processing:
    1. Checks for errors and sets appropriate flags
    2. Formats text output with system messages if present
    3. Processes base64 image data if available
    4. Constructs standardized API response format
    """

# Core function: _response_to_params
def _response_to_params(response: BetaMessage) -> list[BetaTextBlockParam | BetaToolUseBlockParam]:
    """
    Converts API response into internal parameter format.
    Functionality:
    - Processes text blocks from response
    - Handles tool use blocks
    - Maintains type safety with explicit casting
    - Preserves message structure for further processing
    """

# Core function: _maybe_prepend_system_tool_result
def _maybe_prepend_system_tool_result(result: ToolResult, result_text: str):
    """
    Handles system message integration with tool results.
    Features:
    - Conditionally prepends system messages
    - Maintains message format consistency
    - Preserves original tool output
    """
